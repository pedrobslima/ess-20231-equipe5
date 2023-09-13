import { ReactNode } from "react";
import { createContext, useState } from "react";

interface UserContextProps {
  loggedUser;
  setLoggedUser;
}

export const UserContext = createContext<UserContextProps>(
  {} as UserContextProps
);

interface UserProviderProps {
  children: ReactNode;
}

export const PostProvider = ({ children }: UserProviderProps) => {
  const [loggedUser, setLoggedUser] = useState("");
  
  // botar coisas

  return (
    <UserContext.Provider
      value={{
        loggedUser,
        setLoggedUser
      }}
    >
      {children}
    </UserContext.Provider>
  );
};