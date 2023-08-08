import styles from "./index.module.css";
import { Link } from "react-router-dom";
import Button from "../../../../shared/components/Button";
import axios from 'axios';
import React, { useState, useEffect } from 'react';
import { forEach } from "cypress/types/lodash";

const Postagem = (id) => {
  
  const [retorno, setRetorno] = useState(null);
  
  useEffect(() => {
    async function fetch() {
      try {
        //console.log(id[0])
        //const response = await axios.get(`http://127.0.0.1:8000/post?ids=${id[0]}`);
        const response = await axios.get(`https://teste-fastapi.vercel.app/post?ids=${id[0]}`);
        
        const aux = Object.values(response.data);
        setRetorno(aux[0]);
        console.log(aux[0]);
      } catch (error) {
        window.alert(error);
      }
    }

    fetch();
  }, []);

  useEffect(() => {
    console.log(retorno);
  }, [retorno]);


  return (
  <div className={styles.container}>
    {
    retorno == null ?
      <span className={styles.loading}>Carregando...</span>
        :
      <div className={styles.aux}>
        <div className={styles.topbar}>
          <span className={styles.post_tittle}>{retorno.title}</span>
          <span className={styles.post_user}>{retorno.user}</span>
        </div>
        <div className={styles.middle_bar}>
          <span className={styles.post_body}>{retorno.body}</span>
        </div>
        <div className={styles.post_tags}>
          <span>tags:</span>
          <a href="">pokemon</a>
          <a href="">pokemon</a>
        </div>
      </div>
    }
  </div>
  );
};

export default Postagem;
