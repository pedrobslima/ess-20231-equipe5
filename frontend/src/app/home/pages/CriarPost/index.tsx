import styles from "./index.module.css";
import { Link } from "react-router-dom";
import axios from 'axios';
//import React from 'react';
import React, { Component } from 'react';

export default class CriarPost extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      user: '',
      title: '',
      body: '',
      tags: '',
      botaoDesabilitado: true
    };

    this.submitPost  = this.submitPost.bind(this);
    this.handleInputChange  = this.handleInputChange.bind(this);
  }
  
  handleInputChange (event) {
    const { name, value } = event.target;
    this.setState({ [name]: value }, () => {
      const { user, title, body, tags } = this.state;
      const botaoDesabilitado = !(user !== '' && title !== '' && body !== '' && tags !== '');
      this.setState({ botaoDesabilitado });
    });
  }
    

  async submitPost (event) {
    event.preventDefault();
    const state = { user: this.state.user, title: this.state.title, body: this.state.body, tags: this.state.tags };
    console.log(state);
    try {
      //const response = await axios.post('http://127.0.0.1:8000/post', this.state);
      const response = await axios.post('https://teste-fastapi.vercel.app/post', this.state);
      console.log(response.data);
    } catch (error) {
      window.alert(error);
    }
  }
  
  render() {
    return (<section className={styles.container}>
      <h1 className={styles.title}>Crie um post</h1>
      <form className={styles.formContainer} onSubmit={this.submitPost}>
        <div className={styles.user_title}>
          <input
            name="user"
            value={this.state['user']}
            id="input-user"
            data-cy="input-user"
            placeholder="username"
            className={`${styles.input_bar} ${styles.input_user}`}
            onChange={this.handleInputChange}
          />
          <input
            name="title"
            value={this.state['title']}
            id="input-title"
            data-cy="input-title"
            placeholder="title"
            className={`${styles.input_bar} ${styles.input_title}`}
            onChange={this.handleInputChange}
          />
        </div>
        <textarea 
            name="body"
            value={this.state['body']}
            id="input-body"
            data-cy="input-body"
            placeholder="type here..."
            className= {`${styles.input_bar} ${styles.input_body}`}
            onChange={this.handleInputChange}
          />
        
        <div className={styles.tags_container}>
            <span>tags:</span>
            <input
              name="tags"
              value={this.state['tags']}
              id="input-tags"
              data-cy="input-user"
              placeholder="ex: tag1, tag2"
              className={`${styles.input_bar} ${styles.input_user}`}
              onChange={this.handleInputChange}
            />
          </div>

        <button id="botao" data-cy="create" type="submit" className={styles.botao} disabled={this.state.botaoDesabilitado}>
          post
        </button>

        <Link data-cy="view-tests" to="/search">
          BUSCAR POSTS
        </Link>
      </form>
    </section>);
  }

}

