import { useState, useEffect } from 'react';
import { useNavigate, useParams } from "react-router-dom";
//import { UserContext } from "../../context/UserContext";
import { api } from '../../../../shared/services/ApiService';
import Comment from '../../components/Comment'
//import axios from "axios";
//import { toBase64 } from "../../../../shared/services/base64.js";
import './postPage.css';

function postPage() {
    //const { user, setUser, title, setTitle, tags, setTags, body, setBody, image, setImage, comments, setComments } = useContext(PostContext);
    const navigate = useNavigate();
    //const { loggedUser } = useContext(UserContext);
    const [user, setUser] = useState("");
    const [tags, setTags] = useState([]);
    const [title, setTitle] = useState("");
    const [body, setBody] = useState("");
    const [img_name, setImgName] = useState(undefined);
    const [img_content, setImgContent] = useState(undefined);
    const [comments, setComments] = useState([]);
    const { postId } = useParams();
    console.log('postId: ' + postId) 

    function clck_new_comment(){
        navigate('post/' + postId + '/new_comment', {state: {
            og_postId: postId
        }});
    };

    useEffect(() => {
        const getPostInfo = async () => {
            try {
                const response = await api.get('post/' + postId);
                setUser(response.data.data.user);
                setTags(response.data.data.tags);
                setTitle(response.data.data.title);
                setBody(response.data.data.body);
                setImgName(response.data.data.image_name);
                //setImgContent(response.data.image_content);
                setComments(response.data.data.comments);
            } catch (error) {
                console.log('Erro: ' + error);
            }
        };

        getPostInfo();

    }, []); // se o [] tiver vazio ele só vai executar uma vez quando abrir

    return (
        <div className="Page">
            <div className="PostHeader">
                <div className="user">
                    <p> {user} </p>
                </div>
                <div className="title">
                    <p> {title} </p>
                </div>
                <div className="tags">
                <p> {tags} </p>
                </div>
            </div>
            <div className="PostBody">
                <div className="body">
                <p> {body} </p>
                </div>
                {img_name != null && (
                    <div className="body_image">
                        <p>[{img_name}]</p>
                        <img src={img_content} />
                    </div>
                )}
                <div>
                    <button className="CommentButton" onClick={clck_new_comment}>
                        COMENTAR
                    </button>
                </div>
            </div>
            <div>
            {comments.map((comment: Object) => (
                <div className="comments" key={comment.id}>
                    <Comment
                        user={comment.user}
                        text={comment.body}
                    />
                </div>
            ))}
            </div>
        </div>
    );
}

export default postPage;
