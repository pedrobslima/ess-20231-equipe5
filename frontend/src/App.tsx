import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Header from "./app/home/components/header/index";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import EmAlta from "./app/home/pages/EmAlta";
import maisVistos from "./app/home/pages/maisVistos";
import maisBemAvaliados from "./app/home/pages/maisBemAvaliados";
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
    path: "/mais-vistos",
    Component: maisVistos,
  },
  {
    path: "/mais-bem-avaliados",
    Component: maisBemAvaliados,
  },{
    path: "/search",
    Component: Search,
  },
]);

export default function App() {

  return (
    <Header>
      <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
    </Header>
  )
}
