package rmiChat.server;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;

import rmiChat.client.ChatClient;

public class ChatServer extends UnicastRemoteObject  {

	private static final long serialVersionUID = 1L;
	private ArrayList<ChatClient> chatClients;
	
	protected ChatServer() throws RemoteException {
		chatClients = new ArrayList<ChatClient>();
	}

	public synchronized void registerChatClient(ChatClient chatClient){
		this.chatClients.add(chatClient);
	}
	
	public synchronized void deleteChatClient(ChatClient chatClient){
		this.chatClients.remove(chatClient);
	}
	
	public synchronized void broadcastMessage(String message, ChatClient chatClient){
		int i = 0;
		while(i < chatClients.size()){
			if (chatClient != chatClients.get(i)){
				chatClients.get(i).retrieveMessage(message);
				i++;
			}
		}
	}
	
	
}
