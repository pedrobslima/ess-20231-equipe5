import styles from "./index.module.css";

const FeedCard = ({src="", title="", descr=""}) => {
  return (
    <div className={styles.container} style={{backgroundImage:`url(${src})`}}>
      <div className={styles.overlay}>
        <h1 className={styles.title}>{title}</h1>
        <p className={styles.description}>{descr}</p>
      </div>
    </div>
  );
};

export default FeedCard;
