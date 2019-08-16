package rmiChat.client;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.Scanner;

import rmiChat.server.ChatServer;

public class ChatClient extends UnicastRemoteObject implements Runnable {
	
	private static final long serialVersionUID = 1L;
	
	private String name;
	private ChatServer chatServer;
	boolean registered = false;
	private static Scanner scanner;
	
	protected ChatClient(String name, ChatServer chatServer) throws RemoteException {
		this.name = name;
		this.chatServer = chatServer;
		scanner = new Scanner(System.in);
	}

	public String clientID(){
		return name;
	}
	
	public void retrieveMessage(String message) {
		System.out.println(message);	
	}

	public void registerServer(ChatServer chatServer){
		chatServer.registerChatClient(this);
	}
	
	private static String mainMenu() {
		System.out.println("================================");
		System.out.println("RMI Client");
		System.out.println("Selecione a opção desejada");
		System.out.println("================================");
		System.out.println(" [1] Solicitar participação na lista de mensagens");
		System.out.println(" [2] Solicitar saida da lista de mensagens");
		System.out.println(" [3] Enviar mensagem ao servidor");
		System.out.println(" [4] Visualizar mensagens recebidas");
		System.out.println("Coloque a opcao desejada : ");
		return scanner.nextLine();
	}
	
	public void run(){
		
		String message;
		while(true){
			switch(mainMenu()){
				case "1":
					if (!registered){
						this.registerServer(chatServer);
						registered = true;
					}
					else{
						System.out.println("Cliente já registrado");
					}
					break;
			
				case "2":
					if (registered){
						chatServer.deleteChatClient(this);
						registered = false;
					}
					else{
						System.out.println("Cliente não está registrado");
					}
					break;
				case "3":
					message = scanner.nextLine();
					chatServer.broadcastMessage(name+" : "+message, this);
					break;
			}
			
		}
	}
}
