import styles from "./index.module.css";
import axios from "axios";
import { useEffect, useRef, useState } from "react";




const EmAlta = () => {

    const ulRef = useRef<HTMLUListElement>(null);
    const [atual, setLista] = useState<any>([]);
    
    const carregarAnimesDia = async () => {

        const response = await axios.get('http://localhost:8000/emalta/dia');
        const objectNames = Object.values(response.data as any).map(anime => (anime as any).nome_anime);
        setLista(objectNames);
                
    };

    const carregarAnimesSemana = async () => {

        const response = await axios.get('http://localhost:8000/emalta/semana');
        const objectNames = Object.values(response.data as any).map(anime => (anime as any).nome_anime);
        setLista(objectNames);
                
    };

    const carregarAnimesTrimestre = async () => {

        const response = await axios.get('http://localhost:8000/emalta/trimestre');
        const objectNames = Object.values(response.data as any).map(anime => (anime as any).nome_anime);
        setLista(objectNames);
                
    };

    const carregarAnimesAno = async () => {

        const response = await axios.get('http://localhost:8000/emalta/ano');
        const objectNames = Object.values(response.data as any).map(anime => (anime as any).nome_anime);
        setLista(objectNames);
                
    };

    useEffect(() => {
        
        carregarAnimesDia();
        carregarAnimesSemana();
        carregarAnimesTrimestre();
        carregarAnimesAno();
    }, []);

        
    return (
        <section>
            <h1>Em Alta</h1>

            <div className={styles.container}>DIA</div>
                <button>show</button>

                <ul>
                    {atual.map((elem)=>(
                        <li key={elem}>{elem}</li>
                    ))}
                </ul>

            <div className={styles.container}>SEMANA</div>
                <button>show</button>

                <ul>
                    {atual.map((elem)=>(
                        <li key={elem}>{elem}</li>
                    ))}
                </ul>

            <div className={styles.container}>TRIMESTRE</div>
                <button>show</button>

                <ul>
                    {atual.map((elem)=>(
                        <li key={elem}>{elem}</li>
                    ))}
                </ul>

            <div className={styles.container}>ANO</div>
                <button>show</button>

                <ul>
                    {atual.map((elem)=>(
                        <li key={elem}>{elem}</li>
                    ))}
                </ul>
                
            
        </section>
    )
};

export default EmAlta;