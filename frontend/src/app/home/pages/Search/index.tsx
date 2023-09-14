import styles from "./index.module.css";
import Tag from "../../components/tag/index";
import { useLocation } from "react-router-dom";
import { useEffect, useState } from "react";

const Search = () => {
  
  const location = useLocation();
  const [tags, setTags] = useState([] as string[]);
  
  useEffect(() => {
      const queries_ = window.location.href.split("tags=")[1];

      if (queries_ != null) {
        const tags_ = queries_.split(",");
        setTags( tags_.filter(item => item !== ""));
      } else {
        setTags( []);
      }
      
  }, [location]);
  
  return (
    <section className={styles.container}>
      <h1 className={styles.title}>Tela de Pesquisa</h1>
      <span>
        {(tags.length > 0) ? <span>pesquisou por: </span> : null}
        {tags.map((tag, index) => { return <Tag key={index} tag={tag}/> })}
      </span>
    </section>
  );
};

export default Search;


