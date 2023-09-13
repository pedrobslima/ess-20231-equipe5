import styles from "./index.module.css";

const Tag = ({tag="empty", text="#222", bg="#999"}) => {

  return (
    <span className={styles.tag} style={{backgroundColor: `${bg}`, color:`${text}`}}>
        {tag}
    </span> 
  );
};

export default Tag;