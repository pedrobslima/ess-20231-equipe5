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
                <div className="btn-group">
                    <a href="#" className="btn btn-primary active" aria-current="page">Dia</a>
                    <a href="#" className="btn btn-primary">Semana</a>
                    <a href="#" className="btn btn-primary">Trimestre</a>
                    <a href="#" className="btn btn-primary">Ano</a>
                    </div>
                <table className="table table-dark table-striped">
                    <tr>
                        <th>Animes</th>
                        <th>Qtd. Assistidos</th>
                    </tr>
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

export default EmAlta;