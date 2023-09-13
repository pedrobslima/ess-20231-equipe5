import styles from "./index.module.css";
/*import { SubmitHandler, useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { useContext, useEffect } from "react";
import { HomeContext } from "../../context/HomeContext";
import { TestFormSchema, TestFormType } from "../../forms/TestForm";
import { Link } from "react-router-dom";
import Button from "../../../../shared/components/Button";*/
import Tag from "../../components/tag/index";

const Search = () => {
  const tags = window.location.href.split("tags=")[1].split(",");

  const conteudo = [
    {},
    {},
  ];
  
  return (
    <section className={styles.container}>
      <h1 className={styles.title}>Tela de Pesquisa</h1>
      <span>
        pesquisou por:
        {tags.map((tag) => { return <Tag tag={tag}/> })}
      </span>
    </section>
  );
};

export default Search;


