import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import EmAlta from "./app/home/pages/EmAlta";
import EmAltaSemana from "./app/home/pages/EmAltaSemana";
import EmAltaTrimestre from "./app/home/pages/EmAltaTrimestre";
import EmAltaAno from "./app/home/pages/EmAltaAno";
import maisVistos from "./app/home/pages/maisVistos";
import maisBemAvaliados from "./app/home/pages/maisBemAvaliados";

const router = createBrowserRouter([
  {
    path: "*",
    Component: CreateTest,
  },
  {
    path: "/create-test",
    Component: CreateTest,
  },
  {
    path: "/tests",
    Component: ListTests,
  },
  {
    path: "/emalta",
    Component: EmAlta,
  },
  {
    path: "/emalta/dia",
    Component: EmAlta,
  },
  {
    path: "/emalta/semana",
    Component: EmAltaSemana,
  },
  {
    path: "/emalta/trimestre",
    Component: EmAltaTrimestre,
  },
  {
    path: "/emalta/ano",
    Component: EmAltaAno,
  },
  {
    path: "/mais-vistos",
    Component: maisVistos,
  },
  {
    path: "/mais-bem-avaliados",
    Component: maisBemAvaliados,
  }
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
