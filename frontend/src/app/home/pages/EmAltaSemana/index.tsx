import styles from "./index.module.css";
import axios from "axios";
import { useEffect, useRef, useState } from "react";




const EmAltaSemana = () => {
    const [animeList, setAnimelist] = useState([]);

    const getAnimesSemana = async() => {

        const response = await axios.get('http://localhost:8000/emalta/semana');
        setAnimelist(response.data);
    }

    useEffect(() => {
        
        getAnimesSemana();

    }, []);

        
    return (
        <section>
            <div>
                <h2>Em Alta</h2>
                <div className="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
                    <div className="btn-group me-2">
                        <a href="http://localhost:3000/emalta/dia" className="btn btn-secondary">Dia</a>
                        <a href="#" className="btn btn-secondary active" aria-current="page">Semana</a>
                        <a href="http://localhost:3000/emalta/trimestre" className="btn btn-secondary">Trimestre</a>
                        <a href="http://localhost:3000/emalta/ano" className="btn btn-secondary">Ano</a>
                    </div>
                    <div className="btn-group me-2">
                        <a href="http://localhost:3000/analise-de-tendencias" className="btn btn-secondary me-md-2">↵ Voltar</a>
                    </div>
                </div>    
                <table className="table">
                <caption>Em Alta na semana</caption>
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

export default EmAltaSemana;