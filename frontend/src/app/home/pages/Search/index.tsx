import styles from "./index.module.css";
import Tag from "../../components/tag/index";
import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";
import SearchResult from "../../components/searchResult";


const Search = () => {
  
  const location = useLocation();
  const [tags, setTags] = useState([] as string[]);
  const [posts, setPosts] = useState([] as string[]);
  const [blank, setBlank] = useState(false);
  
  useEffect(() => {
      const queries_ = window.location.href.split("tags=")[1];

      if (queries_ != null) {
        const tags_ = queries_.split(",");
        setTags( tags_.filter(item => item !== ""));
      } else
        setTags([]);      
      
      axios.get(`http://127.0.0.1:8000/search?tags=${queries_}`)
        .then(response => {
          if (response.data.status_code == 200) {
            setPosts(response.data.data.matches);
            setBlank(false);
          } else {
            setPosts([]);
            setBlank(true);
          }
        })
        .catch(error => {
          console.error(error);
      });
      
  }, [location]);
  
  return (
    <section className={styles.container}>
      <div className={styles.tags}>
        {tags.map((tag, index) => { return <Tag key={index} tag={tag}/> })}
      </div>
        
      { blank ? <span className={styles.noResults}>Nenhum resultado encontrado</span>:
        <div className={styles.results}>
          {posts.map((post, index) => { return <SearchResult key={index} post_id={post}/> })}
        </div>
      }

    </section>
  );
};

export default Search;


