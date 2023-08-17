import sqlite3;
from db.CreatePost import CreatePost;
from db.SearchPost import SearchPost;
from uuid import uuid4
from base64 import b64decode
import os

class server_bd():
    
    def __init__(self, url: str):
        self.db = url
        self.connect()
    
        try:        
            self._cur.execute('SELECT * FROM Post')
            self._cur.execute('SELECT * FROM Post_tag')
            self._cur.execute('SELECT * FROM Comments')
            print("[sucesso] Conectado ao banco com sucesso."); 
        except sqlite3.OperationalError:

            try:
                self._cur.execute('DROP TABLE Post')
            except sqlite3.OperationalError:
                pass
            try:
                self._cur.execute('DROP TABLE Post_tag')
            except sqlite3.OperationalError:
                pass
            try:
                self._cur.execute('DROP TABLE Comments')
            except sqlite3.OperationalError:
                pass
            
            self._cur.execute('CREATE TABLE Post(id, user, title, body, image)')
            self._cur.execute('CREATE TABLE Post_tag (post, tag)')
            self._cur.execute('CREATE TABLE Comments(id, post, user, body)')
            
            print("[aviso] Tabelas 'Post', 'Comments' e 'Post_tag' foram criadas.")
            self.settle()
        finally:
            self.c_post = CreatePost(self.cur)
            self.s_post = SearchPost()
            self.disconnect()
    
    def connect(self):
        '''Estabilish connection to database\n 
        (need to make sure it doesn't cause any multithreading problems)'''
        print('conectou')
        self._con = sqlite3.connect(self.db, check_same_thread=False)
        self._cur = self._con.cursor()

    def disconnect(self):
        '''Closing connection to database'''
        print('desconectou')
        self._cur.close()
        self._con.close()

    def settle(self):
        self._cur.execute('SELECT * FROM Post')
        count = len(self._cur.fetchall())
        #print(count)
        if(count > 0):
            return False

        db = CreatePost(self._cur)
        db.criaPost( {'user': 'vinicius13', 'title': "pokemon eh massa", 'body': 'to gostando mto dos ultimos episodios. E vcs?', 'tags':['pokemon', 'anime']})
        db.criaPost( {'user': 'vinicius13', 'title': 'pokemon >> digimon', 'body': 'digimon eh paia dms kk', 'tags':['pokemon', 'digimon', 'humor']})
        db.criaPost( {'user': 'marquinh0s', 'title': 'one piece ta em hiato eh?', 'body': 'faz um tempo q n tem capitulo novo. Algm sabe?', 'tags':['one piece', 'op', 'gear 5', 'mangá']})
        db.criaPost( {'user': 'verona', 'title': 'party de genshin', 'body': 'alguma alma caridosa ta afim de me ajudar numa campnha nivel 8?', 'tags':['games', 'genshin impact', 'garena']})
        db.criaPost( {'user': 'aldebaram', 'title': 'esse seya eh um canalha', 'body': 'o bixo me atacou de costas,boy. isso n existe n. E olha q eu tava pegando leve com esse bixo visse', 'tags':['cdz']})
        db.criaPost( {'user': 'aiorus', 'title': 'counter pra ikki de fenix', 'body': 'tipo assim.. o cara sempre volta? alguem sabe alguma forma de causar morte morrida no cara?', 'tags':['cdz', 'cavaleiros do zodiaco']})
        db.criaPost( {'user': 'eren', 'title': 'tatakae', 'body': 'tatakae', 'tags':['aot', 'anime']})
        db.criaPost( {'user': 'pikachu', 'title': 'great ball', 'body': 'mais espacosa que a comum, menos confortavel que a ultra. Pelo preco acho que vale a pena', 'tags':['pokemon', 'humor']})
        self._con.commit()

        return True
    
    def getPost(self, post_id: str) -> dict | None:
        '''Get post by id

        Parameters
        - post_id: 
            The id of the comments original post    

        Returns
        - post: 
            A dictionary containing the posts info
        - None
            In case it doesn't find the post
        '''
        self.connect()

        self._cur.execute(f"SELECT * FROM Post WHERE id = {post_id}")
        
        main_post = self._cur.fetchone()

        self._cur.execute(f"SELECT * FROM Post_tag")
    
        self.disconnect()
        
        return {main_post[0]: 
                {'user': main_post[1],
                 'title': main_post[2],
                 'body': main_post[3]}}

    def createPost(self, post: dict, post_img: bytes | None = None) -> dict | None:
        '''
        Will try to choose a random id for the post, create and then store it (and its image) in the database.
        If it can't generate an unused id after 3 tries, it gives up. 

        Parameters
        - post:
            A dicitionary containing all of the posts data:
                - user
                - list of tags
                - title
                - body
                - images file name
        - post_img:
            Contains the bytes that make up the posts attached image

        Returns
        - new_post: 
            The id and the new post uploaded to the forum in a form of dictionary
        '''
        self.connect()

        count = 0
        p_check = True
        self._cur.execute(f'SELECT id FROM Post')
        id_list = self._cur.fetchall()
        while(p_check and count<3):
            post_id = str(uuid4())
            p_check = post_id in id_list
            count += 1

        if(not p_check):
            self._cur.execute(
                'INSERT INTO Post (id, user, title, body, image) VALUES (?, ?, ?, ?, ?)',
                (post_id, post["user"], post["title"], post["body"], post["img_filename"])
            )
            tags = [(post_id, tag.capitalize()) for tag in post['tags']]
            self._cur.executemany(
                'INSERT INTO Post_tag (post, tag) VALUES (?, ?)',
                tags
            )
            self._con.commit()
            if(post_img is not None):
                content = b64decode(post_img.encode())
                file = open(f'src//db//images//{post["img_filename"]}', 'wb')
                file.write(content)
                file.close()
                #img_repo = os.getcwd()+'/backend/src/db/images'
                #if not os.path.exists(img_repo):
                #    os.makedirs(img_repo)
                #with open(f'{img_repo}/{post["img_filename"]}', 'wb') as f:
                #    f.write(post_img)
            self.disconnect()
            #return {post_id: post}
            #post["post_id"] = post_id
            return post
        self.disconnect()
    
    def search_for_tags(self, tags):

        command = ''
        inner_format = ' INNER JOIN post_tag TAG{0} ON PT.post = TAG{0}.post AND TAG{0}.tag = "{1}"'
        
        for index in range(0, len(tags)):
            command += inner_format.format(index, tags[index])

        self.connect()
        self.cur.execute(f'SELECT PT.post FROM post_tag PT {command} GROUP BY PT.post ORDER BY PT.post DESC')
        
        retorno = {'matches': []}
        for post in self.cur.fetchall():
            retorno['matches'].append(post[0]);
        
        self.disconnect()
        return retorno

    
    def getAllPosts(self):
        self.connect()
        self.cur.execute('SELECT * FROM post')
        
        retorno = self.cur.fetchall()
        self.disconnect()

        return retorno

    def getAllTags(self):
        self.connect()
        self._cur.execute('SELECT tag FROM Post_tag GROUP BY tag')
        tags_list = self._cur.fetchall()
        self.disconnect()
        return tags_list
    
    def getComments(self, post_id: str) -> list | None:
        '''Get a list of comments by a posts id

        Parameters
        - post_id: 
            The id of the comments original post    

        Returns
        - A list of comments of the searched post
        '''
        self.connect()

        post = self.getPost(post_id)

        if(not post):
            return None

        self._cur.execute(f'SELECT * FROM Comments WHERE post = {post_id}')

        post[post_id]['comments'] = self._cur.fetchall()

        self.disconnect()

        return post

    def createComment(self, comment: dict, post_id: str) -> bool | None:
        '''Create a comment (explain more later)'''
        self.connect()

        if(self.getPost(post_id)):
            count = 0
            c_check = True
            self._cur.execute(f'SELECT id FROM Comments WHERE post = {post_id}')
            id_list = self._cur.fetchall()
            while(c_check and count<3):
                comment_id = uuid4()
                c_check = comment_id in id_list
                count += 1

            if(not c_check):
                self._cur.execute(f'INSERT INTO Comment * VALUES ({comment_id}, {post_id}, "{comment["user"]}", "{comment["body"]}")')
                self._con.commit()
                self.disconnect()
                return True
            self.disconnect()
            return False


    @property
    def con(self):
        return self._con

    @con.setter
    def con(self, param):
        return None

    @property
    def cur(self):
        return self._cur

    @cur.setter
    def cur(self, param):
        return None

server_ = server_bd("banco.db")
