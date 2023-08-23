import sqlite3

class SearchPost:
    def __init__(self):
        pass
    
    def searchForTags(self, tags, cursor):
        inner_format = ' INNER JOIN post_tag TAG{0} ON PT.post = TAG{0}.post AND TAG{0}.tag = "{1}"'
        
        command = ''
        for index in range(0, len(tags)):
            command += inner_format.format(index, tags[index])
        
        cursor.execute(f'SELECT PT.post FROM post_tag PT {command} GROUP BY PT.post ORDER BY PT.post DESC')
        
        retorno = {'matches': []}
        for post in cursor.fetchall():
            retorno['matches'].append(post[0]);
        
        return retorno

    def getPosts(self, ids, cursor):
        ids_ = 'id = {0}'.format(ids[0]);
        for index in range(1, len(ids)):
            ids_ = ids_ + (' OR id = {0}'.format(ids[index]));

        cursor.execute('SELECT * FROM post WHERE ' + ids_);
        return cursor.fetchall();

    def getAll(self, cursor):
        cursor.execute('SELECT * FROM post');
        return cursor.fetchall();

    def existingTags(self, cursor):
        cursor.execute('SELECT tag FROM post_tag GROUP BY tag ORDER BY tag ASC');
        return cursor.fetchall();
