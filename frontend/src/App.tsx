import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CreateTest from "./app/home/pages/CreateTest";
import ListTests from "./app/home/pages/ListTests";
import EmAlta from "./app/home/pages/EmAlta";
import maisVistos from "./app/home/pages/maisVistos";
import maisBemAvaliados from "./app/home/pages/maisBemAvaliados";
import postPage from "./app/home/pages/postPage";

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
  },
  {
    path: "/post/:postId",
    Component: postPage,
  }
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
}
