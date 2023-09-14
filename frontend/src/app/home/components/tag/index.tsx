import styles from "./index.module.css";
import { Link } from "react-router-dom";

const Tag = ({tag="empty", text="#222", bg="#999"}) => {
  return (
    <Link to={`/search?tags=${tag}`} replace className={styles.tag} style={{backgroundColor: `${bg}`, color:`${text}`}}>
      {tag}
    </Link>
  );
};

export default Tag;
