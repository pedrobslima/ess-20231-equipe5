import { useState, useContext } from 'react';
//import { useForm, SubmitHandler } from "react-hook-form"
import { useNavigate } from "react-router-dom";
import { UserContext } from "../../context/UserContext";
import { api } from '../../../../shared/services/ApiService';
//import { ImgUpContext } from '../../context/ImgUpContext';

function CreatePost() {
    const navigate = useNavigate();
    const { loggedUser } = useContext(UserContext);
    //const { file, imagePreview, base64, name, onChange, _handleReaderLoaded, onFileSubmit, photoUpload, remove } = useContext(ImgUpContext);
    const [tagInput, setTagInput] = useState(''); // Para controlar o campo de entrada de tags
    const [post, setPost] = useState({
        user: loggedUser,
        tags: [] as string[],
        title: "",
        body: "",
        img_name: null as null | string,
        img_content: null as null | string | ArrayBuffer
    });
    //-----------------
    const handleChange = (event) => {
        const { name, value} = event.target;
        setPost({
            ...post,
            [name]: value,
        });
        console.log(name + ': ' + value);
    };

    const readImageAsBase64 = async (file) => {
        const reader = new FileReader();
      
        reader.onloadend = (e) => {
            if(e.target != null){
                const base64Image = e.target.result;
                setPost({
                    ...post,
                    img_name: file.name,
                    img_content: base64Image
                }); 
            }
        };
      
        reader.readAsDataURL(file);
    };

    const handleImageUpload = async (e) => {
        const file = e.target.files[0];

        if (file) {
            readImageAsBase64(file);
        }        
    };

    const removeFile = async () => {
        setPost({
            ...post,
            img_name: null,
            img_content: null
        });
    }

    const handleTagInputChange = (event) => {
        setTagInput(event.target.value);
    };
    
    const addTag = () => {
        if (tagInput.trim() !== '' && !post.tags.includes(tagInput.trim())) {
            setPost({
                ...post,
                tags: [...post.tags, tagInput.trim()],
            });
        }
        setTagInput('');
    };

    const removeTag = (deadTag) => {
        const updatedTags = post.tags.filter((tag) => tag !== deadTag);
        setPost({
            ...post,
            tags: updatedTags,
        });
    };

    const handleSubmit = async () => {
        if (post.body === '' || post.title === '') {
            alert('Para realizar uma postagem, os campos de título e corpo precisam ser preenchidos.');
            return; // Impedir o envio se o corpo estiver em branco
        }
        
        const response = await api.post(location.pathname, post);
        console.log(response.data);

        setPost({
            user: loggedUser,
            tags: [],
            title: "",
            body: "",
            img_name: null,
            img_content: null
        });

        navigate('/post/' + response.data.data.post_id); // abre tela do post criado
    };   

    const onSubmit = async (event) => {
        event.preventDefault();
        handleSubmit();
    };

    return (
        <div className="Page">
            <div className="user">
                {loggedUser}
            </div>
            <form onSubmit={onSubmit}>
                <div className="title">
                    <label>
                        Título:
                        <input
                            type="text"
                            name="title"
                            value={post.title}
                            onChange={handleChange}
                        />
                    </label>
                </div>
                <div className="tags">
                    <label>
                        Tags:
                        <input
                            type="text"
                            value={tagInput}
                            onChange={handleTagInputChange}
                        />
                        <button type="button" onClick={addTag}>
                            Adicionar
                        </button>
                    </label>
                </div>
                {post.tags.length > 0 && (
                    <div>
                        <ul>
                            {post.tags.map((tag, index) => (
                                <div key={index}>
                                    <button
                                        type="button"
                                        onClick={() => removeTag(tag)}
                                        >
                                         X 
                                    </button>
                                    {tag}
                                </div>
                            ))}
                        </ul>
                    </div>
                )}
                <div className="body">
                    <label>
                        Corpo:
                        <textarea
                            name="body"
                            value={post.body}
                            onChange={handleChange}
                        />
                    </label>
                </div>
                <div className="image">
                    <label>
                    Imagem:
                    <input
                        type="file"
                        accept=".jpef, .png, .jpg"
                        onChange={handleImageUpload}
                        />
                    </label>
                    {post.img_name != null &&
                        <button type="button" onClick={removeFile} >Remover</button>
                    }
                </div>
                <button type="submit">Postar</button>
            </form>
        </div>
    );
}

export default CreatePost;
