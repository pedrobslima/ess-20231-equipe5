import styles from "./index.module.css";
import {useNavigate} from "react-router-dom";
import { Link } from "react-router-dom";

const Tag = ({tag="empty", text="#222", bg="#999"}) => {
  const navigate = useNavigate();

  const mudarTela = () => {
    navigate(`/search?tags=${tag}`);
  }

  return (
    
    <Link to={`/search?tags=${tag}`} replace className={styles.tag} style={{backgroundColor: `${bg}`, color:`${text}`}}>
      {tag}
    </Link>
  );
};

export default Tag;
