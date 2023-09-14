import { useState, useContext, ChangeEvent, FormEvent } from 'react';
//import { useForm, SubmitHandler } from "react-hook-form"
import { useNavigate, useParams, useLocation } from "react-router-dom";
import { UserContext } from "../../context/UserContext";
import { api } from '../../../../shared/services/ApiService';
import './CreateComment.css';

function CreateComment() {
    const navigate = useNavigate();
    const { loggedUser } = useContext(UserContext);
    const [comment, setComment] = useState({
        user: loggedUser,
        body: ""
    });
    const { postId } = useParams();

    const location = useLocation();

    const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
        setComment({
            user:loggedUser, 
            body: event.target.value
        });
        console.log('Body: ' + comment.body);
      };

    const handleSubmit = (event: FormEvent) => {
        event.preventDefault();

        if (comment.body === '') {
            alert('Preencha o corpo do comentário.');
            return; // Impedir o envio se o corpo estiver em branco
        }

        console.log('Body: ' + comment.body);
        
        api.post(location.pathname, comment)
            .then((response) => {
                console.log('response: ' + response.data);
            })
            .catch((error) => {
                console.error('Erro ao enviar o formulário: ', error);
            });

        setComment({
            user: loggedUser,
            body: ""
        });

        navigate('/post/' + postId);
    };

    return (
        <div className="Page">
            <div className="OriginalPostInfo">
                <div className="user">
                    <p>{location.state.og_user}</p>
                </div>
                <p>{location.state.og_body}</p>
            </div>
            <div className="CommentHeader">
                <div className="user">
                    {loggedUser}
                </div>
            </div>
            <div className="CommentBody">
                <form onSubmit={handleSubmit}>
                    <p>Comentário:</p>
                    <label>
                        <input
                            type="text"
                            value={comment.body}
                            onChange={handleChange}
                        />
                    </label>
                    <button type="submit">Enviar</button>
                </form>
            </div>
        </div>
    );
}

export default CreateComment;
