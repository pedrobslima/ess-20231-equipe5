import styles from "./index.module.css";
import axios from "axios";
import { useEffect, useRef, useState } from "react";




const EmAltaTrimestre = () => {
    const [animeList, setAnimelist] = useState([]);

    const getAnimesTrimestre = async() => {

        const response = await axios.get('http://localhost:8000/emalta/trimestre');
        setAnimelist(response.data);
    }

    useEffect(() => {
        
        getAnimesTrimestre();

    }, []);

        
    return (
        <section>
            <div>
                <h2>Em Alta</h2>
                <div className="btn-group">
                    <a href="http://localhost:3000/emalta/dia" className="btn btn-primary">Dia</a>
                    <a href="http://localhost:3000/emalta/semana" className="btn btn-primary">Semana</a>
                    <a href="#" className="btn btn-primary active" aria-current="page">Trimestre</a>
                    <a href="http://localhost:3000/emalta/ano" className="btn btn-primary">Ano</a>
                    </div>
                <table className="table table-dark table-striped">
                <thead>
                    <tr>
                        <th>Animes</th>
                        <th>Qtd. Assistidos</th>
                    </tr>
                </thead>    
                    <tbody>
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

export default EmAltaTrimestre;