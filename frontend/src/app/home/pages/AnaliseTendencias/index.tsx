import axios from "axios";
import { useEffect, useRef, useState } from "react";




const AnaliseTendencias = () => {

    useEffect(() => {
        
    }, []);

        
    return (
        <section>

            <nav className="navbar navbar-expand-lg bg-body-tertiary">
            <div className="container-fluid">
                <a className="navbar-brand" href="#">Análise de Tendencias</a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                    <li className="nav-item">
                    <a className="nav-link active" aria-current="page" href="#">Página Inicial</a>
                    </li>
                    <li className="nav-item">
                    <a className="nav-link" href="/mais-bem-avaliados">Mais bem-avaliados</a>
                    </li>
                    <li className="nav-item">
                    <a className="nav-link" href="/mais-vistos">Mais vistos</a>
                    </li>
                    <li className="nav-item dropdown">
                    <a className="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Em Alta
                    </a>
                    <ul className="dropdown-menu">
                        <li><a className="dropdown-item" href="/emalta/dia">Em Alta</a></li>
                        <li><a className="dropdown-item" href="/emalta/semana">Em Alta na semana</a></li>
                        <li><a className="dropdown-item" href="/emalta/trimestre">Em Alta no trimestre</a></li>
                        <li><a className="dropdown-item" href="/emalta/ano">Em Alta no ano</a></li>
                    </ul>
                    </li>
                    
                </ul>
                
                </div>
            </div>
            </nav>

        </section>
    )
};

export default AnaliseTendencias