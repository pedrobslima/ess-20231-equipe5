import styles from "./index.module.css";
import { Link } from "react-router-dom";

const Item = ({tag="a"}) => {

  return (
    <Link className={styles.tag} to={`/search?tags=${tag}`} replace>
        <span>{tag}</span>
    </Link>

  );
};

export default Item;
