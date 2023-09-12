import styles from "./index.module.css";

const Topbar = ({ children }) => {

    const side_bar = () => {
        window.alert("abrir sidebar");
    }

    const search = (e) => {

        if (!(e.key === 'Enter'))
            return;

        const el = e.target;
        window.alert(`pesquisar: "${el.value}"`);
    }
    
  return (
    <section className={styles.container}>
        <div className={styles.topbar}>
            <div className={styles.teste}>
                💬
                <span>
                    Aniforum
                </span>
            </div>
            <input type="text" className={styles.text_input} placeholder="pesquisar" onKeyDown={(e) => search(e)}/>
            

            <div className={styles.teste} onClick={side_bar}>☰</div>
        </div>
        <div className={styles.children}>
            { children }
        </div>
    </section>
  );
};

export default Topbar;
