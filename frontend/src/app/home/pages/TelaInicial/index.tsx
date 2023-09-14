import styles from "./index.module.css";
import { Link } from "react-router-dom";

const CreateTest = () => {


  return (
    <section className={styles.container}>
      <h1 className={styles.title}>Bem Vindo!</h1>
      <div className={styles.boxContainer}>
        <ul>          
          <li>
            <Link to="/emalta" replace>
              Em Alta
            </Link>
          </li>
          <li>
            <Link to="/mais-vistos" replace>
              Mais Vistos
            </Link>
          </li>
          <li>
            <Link to="/mais-bem-avaliados" replace>
              Mais Bem Avaliados
            </Link>
          </li>
          <li>
            <Link to="/analise-de-tendencias" replace>
              Analise de Tendencias
            </Link>
          </li>
          <li>
            <Link to="/search" replace>
              Tela de Busca
            </Link>
          </li>
          
        </ul>
      </div>
    </section>
  );
};

export default CreateTest;
