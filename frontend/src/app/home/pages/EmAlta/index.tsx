import styles from "./index.module.css";
import axios from "axios";
import { useEffect, useRef, useState } from "react";




const EmAlta = () => {
    const [animeList, setAnimelist] = useState([]);

    const getAnimes = async() => {

        const response = await axios.get('http://localhost:8000/emalta/dia');
        setAnimelist(response.data);
    }

    useEffect(() => {
        
        getAnimes();

    }, []);

        
    return (
        <section>
            <div>
                <h2>Em Alta</h2>
                <div className="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">    
                    
                    <div className="btn-group me-2">
                        <a href="#" className="btn btn-secondary active" aria-current="page">Dia</a>
                        <a href="/emalta/semana" className="btn btn-secondary">Semana</a>
                        <a href="/emalta/trimestre" className="btn btn-secondary">Trimestre</a>
                        <a href="/emalta/ano" className="btn btn-secondary">Ano</a>
                    </div>
                    <div className="btn-group me-2">
                    <a href="/analise-de-tendencias" className="btn btn-secondary me-md-2">↵ Voltar</a>
                    </div>
                </div>    
                <table className="table">
                    <caption>Em Alta no dia</caption>
                <thead className="table-light">    
                    <tr>
                        <th>Animes</th>
                        <th>Qtd. Assistidos</th>
                    </tr>
                </thead>    
                    <tbody className="table-group-divider">
                        {animeList.map((anime) => (
                            <tr key={(anime as any).id}>
                                <th>{(anime as any).nome_anime}</th>
                                <th>{(anime as any).assistidos_periodo}</th>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </section>
    )
};

export default EmAlta;