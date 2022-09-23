import React, { useEffect, useState } from 'react';
import './App.css';

// Custom components
import NavBar from './components/NavBar';
import PublicHome from './components/PublicHome';
import PrivateHome from './components/PrivateHome';

declare type ClientPrincipal = {
  identityProvider: string;
  userId: string;
  userDetails: string;
  userRoles: string[];
};

function App() {
  const [isAuthenticated, userHasAuthenticated] = useState(false);
  const [user, setUser] = useState<ClientPrincipal | null>(null);

  async function getUserInfo() {
    try {
      const response = await fetch('/.auth/me');
      const payload = await response.json();
      const { clientPrincipal } = payload;

      if (clientPrincipal) {
        setUser(clientPrincipal);
        userHasAuthenticated(true);
        console.log(`clientPrincipal = ${JSON.stringify(clientPrincipal)}`);
      }
    } catch (error: any) {
      console.error(`No profile could be found ${error?.message?.toString()}`);
    }
  }

  useEffect(() => {
    getUserInfo();
  }, []);

  return (
    <div className="App">
      <NavBar user={user} />
      <main className="column">
        {isAuthenticated ? <PrivateHome user={user} /> : <PublicHome />}
      </main>
    </div>
  );
}

export default App;
