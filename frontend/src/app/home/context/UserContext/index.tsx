import { ReactNode } from "react";
import { createContext, useState } from "react";

interface UserContextProps {
  loggedUser: string;
  setLoggedUser;
}

export const UserContext = createContext<UserContextProps>(
  {} as UserContextProps
);

interface UserProviderProps {
  children: ReactNode;
}

export const UserProvider = ({ children }: UserProviderProps) => {
  const [loggedUser, setLoggedUser] = useState('pedro12');

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