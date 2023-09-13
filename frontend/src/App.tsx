import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Header from "./app/home/components/header/index";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import EmAlta from "./app/home/pages/EmAlta";
import EmAltaSemana from "./app/home/pages/EmAltaSemana";
import EmAltaTrimestre from "./app/home/pages/EmAltaTrimestre";
import EmAltaAno from "./app/home/pages/EmAltaAno";
import maisVistos from "./app/home/pages/maisVistos";
import maisBemAvaliados from "./app/home/pages/maisBemAvaliados";
import postPage from "./app/home/pages/postPage";
import AnaliseTendencias from "./app/home/pages/AnaliseTendencias";
import Search from "./app/home/pages/Search";

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
  },
  {
    path: "/post/:postId",
    Component: postPage,
  },
  {
    path: "/analise-de-tendencias",
    Component: AnaliseTendencias,
  },
  {
    path: "/search",
    Component: Search,
  }
]);

export default function App() {

  return (
    <Header>
      <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
    </Header>
  )
}
