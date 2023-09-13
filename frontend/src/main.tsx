import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./global.css";
import Provider from "./Provider";
//import Header from "./app/components/header/index.js";
import Header from "./app/home/components/header/index";


ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <Provider>
      <Header>
        <App />
      </Header>
    </Provider>
  </React.StrictMode>
);
