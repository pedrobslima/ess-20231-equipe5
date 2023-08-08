import styles from "./index.module.css";
import { Link } from "react-router-dom";
import Button from "../../../../shared/components/Button";
import axios from 'axios';
import React, { useState, useEffect } from 'react';
import { forEach } from "cypress/types/lodash";
import Postagem from "../Postagem";

export default class CriarPost extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      tags: '',
      response: null,
      disableButton: true
    }
    this.submitSearch  = this.submitSearch.bind(this);
    this.handleInputChange  = this.handleInputChange.bind(this);
  }
   
  async submitSearch (event) {
    event.preventDefault();
      try {
        let temp = this.state.tags;
        temp = temp.replaceAll(/\s/g,'');

        //const response = await axios.get(`http://127.0.0.1:8000/search?tags=${temp}`);
        const response = await axios.get(`https://teste-fastapi.vercel.app/search?tags=${temp}`);
        this.setState({response: response.data.resposta});

        console.log(response.data.resposta);        
      } catch (error) {
        window.alert(error);
      }
  }
   
  handleInputChange (event) {
    const { name, value } = event.target;
    this.setState({ [name]: value }, () => {
      let temp = this.state.tags;
      temp = temp.replaceAll(/\s/g,'');
      
      this.setState({ disableButton: (temp=='') });
    });
  }

  render(){
    return (
      <section className={styles.container}>
        <h1 className={styles.title}>Buscar por Tags</h1>
        <form className={styles.formContainer} onSubmit={this.submitSearch}>
          <div className={styles.search_bar}>
            <input
              id="input-tags"
              name="tags"
              data-cy="input-tags"
              placeholder="tags (ex: humor, pokemon)"
              className={`${styles.input_bar} ${styles.input_tags}`}
              onChange={this.handleInputChange}
            />

            <Button id="botao" data-cy="create" type="submit" className={styles.botao} disabled={this.state.disableButton}>
              search
            </Button>
            
          </div>
          
          {this.state.response === null ? (
            <span>.</span>
          ) : this.state.response.length === 0 ? (
            <span>nenhum post correspondente</span>
          ) : (
            this.state.response.map((post) => <Postagem key={post.id} {...post} />)
          )}

          <Link data-cy="view-tests" to="/">
            CRIAR POSTS
          </Link>
        </form>
      </section>
    );
  }
}

