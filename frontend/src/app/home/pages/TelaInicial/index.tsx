import { SubmitHandler, useForm } from "react-hook-form";
import styles from "./index.module.css";
import { zodResolver } from "@hookform/resolvers/zod";
import { useContext, useEffect } from "react";
import { HomeContext } from "../../context/HomeContext";
import { TestFormSchema, TestFormType } from "../../forms/TestForm";
import { Link } from "react-router-dom";
import Button from "../../../../shared/components/Button";

const CreateTest = () => {
  const { state, prevState, service } = useContext(HomeContext);

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<TestFormType>({
    resolver: zodResolver(TestFormSchema),
  });

  const onSubmit: SubmitHandler<TestFormType> = async (body) => {
    service.createTest(body);
    reset();
  };

  useEffect(() => {
    if (
      state.createTestRequestStatus !== prevState?.createTestRequestStatus &&
      state.createTestRequestStatus.isSuccess()
    ) {
      alert("Teste criado com sucesso!");
    }
  }, [state, prevState]);

  return (
    <section className={styles.container}>
      <h1 className={styles.title}>Bem Vindo!</h1>
      <form className={styles.formContainer} onSubmit={handleSubmit(onSubmit)}>
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
      </form>
    </section>
  );
};

export default CreateTest;
