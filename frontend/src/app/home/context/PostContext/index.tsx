import { ReactNode } from "react";
import { createContext, useState } from "react";
/*import { useNavigate } from "react-router-dom";
import { api } from "../services/api";
import { toBase64 } from "../services/base64";
*/

interface PostContextProps {
  user;
  setUser;
  title;
  setTitle;
  tags;
  setTags;
  body;
  setBody;
  image;
  setImage;
  comments;
  setComments;
}

export const PostContext = createContext<PostContextProps>(
  {} as PostContextProps
);

interface PostProviderProps {
  children: ReactNode;
}

export const PostProvider = ({ children }: PostProviderProps) => {
  const [user, setUser] = useState("");
  const [title, setTitle] = useState("");
  const [tags, setTags] = useState([]);
  const [body, setBody] = useState(null);
  const [image, setImage] = useState(undefined);
  const [comments, setComments] = useState([]);
  
  // botar coisas

  return (
    <PostContext.Provider
      value={{
        user,
        setUser,
        title,
        setTitle,
        tags,
        setTags,
        body,
        setBody,
        image,
        setImage,
        comments,
        setComments
      }}
    >
      {children}
    </PostContext.Provider>
  );
};