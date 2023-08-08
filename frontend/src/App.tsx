import { createBrowserRouter, RouterProvider } from "react-router-dom";
import CriarPost from "./app/home/pages/CriarPost";
import BuscarPost from "./app/home/pages/BuscarPost";

const router = createBrowserRouter([
  {
    path: "*",
    Component: CriarPost,
  },
  {
    path: "/create-post",
    Component: CriarPost,
  },
  {
    path: "/search",
    Component: BuscarPost,
  },
]);

export default function App() {
  return <RouterProvider router={router} fallbackElement={<p>Loading...</p>} />;
  //return <h1>teste</h1>;
}
