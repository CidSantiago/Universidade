package rmiChat.client;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

import rmiChat.server.ChatServer;

public class ChatClientMenu {

	public static void main(String[] args) throws MalformedURLException, RemoteException, NotBoundException {
		String chatServerURL = "rmi://localhost/RMIChatServer";
		ChatServer chatServer = (ChatServer) Naming.lookup(chatServerURL);
		new Thread(new ChatClient(args[0], chatServer)).start();
	}

}
