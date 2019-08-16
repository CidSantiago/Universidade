package twitter.menu;

import twitter.controle.MyTwitter;
import twitter.controle.exceptions.MyTwitterException;
import twitter.perfils.Perfil;
import twitter.perfils.PessoaFisica;
import twitter.perfils.PessoaJuridica;
import twitter.repositorio.RepositorioXML;
import twitter.tweet.Tweet;

import java.util.Locale;
import java.util.Scanner;
import java.util.Vector;

public class Menu {

	private static Scanner scanner = new Scanner(System.in);

	
	public static void main(String[] args) {
		RepositorioXML rep = new RepositorioXML();
		MyTwitter control = new MyTwitter (rep);
		boolean loop = true;
		Perfil usuario = null;
		scanner.useLocale(Locale.US);
		
		while(loop){
			if(usuario == null){
				switch(startMenu()){
				case "1":
					System.out.println("Digite o nome de usuario:");
					String user = scanner.nextLine();
				
					if( rep.buscar(user) != null){
						usuario = rep.buscar(user);
					}
					else{
						System.out.println("Usuario nao encontrado! Tente novamente.");
					}
					
					break;
				
				case "2":
					String id;
					int var;
					Long cpfnj;
					Perfil perfil;
					System.out.println("Qual o tipo de conta desejada?\n1: Pessoa Fisica \n2: Empresa (Pessoa juridica)");
					var = scanner.nextInt();
					if(var == 1){
						System.out.println("Digite o CPF:");
						cpfnj = scanner.nextLong();
						System.out.println("Digite o nome de usuario:");
						scanner.nextLine();
						id = scanner.nextLine();
						perfil = new PessoaFisica(id);
						((PessoaFisica)perfil).setCpf(cpfnj);
					}
					else if (var == 2){
						System.out.println("Digite o CPNJ:");
						cpfnj = scanner.nextLong();
						System.out.println("Digite o nome de usuario:");
						scanner.nextLine();
						id = scanner.nextLine();
						perfil = new PessoaJuridica(id);
						((PessoaJuridica)perfil).setCnpj(cpfnj);
					}
					else{
						System.out.println("Opcao invalida! Repita a operacao");
						break;
					}
					perfil.setAtivo(true);
					
					try{
						control.criarPerfil(perfil);
					}
					catch(MyTwitterException mte){
						System.out.println("Erro! :c \n"+ mte.getMessage());
					}
					
					break;
					
				case "3":
					System.out.println("Ate a proxima! =D");
					usuario = null;
					loop = false;
				
					break;
				
				default:
					break;
				}
			}
			else{
				switch(mainMenu(usuario.getUsuario())){
				
				case "1":
					System.out.println("Digite o tweet desejado");
					String tweet = scanner.nextLine();
					try{
						control.tweetar(usuario.getUsuario(), tweet);
						System.out.println("Tweet submetido! =D");
					}
					catch(MyTwitterException mte){
						System.out.println("Erro! :c \n"+ mte.getMessage());
					}
					break;
				
				case "2":
					System.out.println("Aqui esta sua timeline:");
					try{
						Vector<Tweet> timeline = control.timeline(usuario.getUsuario());
						for (int i = 0; i < timeline.size(); i++){
							printTweet(timeline.get(i));
						}
						System.out.println("Timeline impressa com sucesso! =)");
					}
					catch(MyTwitterException mte){
						System.out.println("Erro! :c \n"+ mte.getMessage());
					}
					
					break;
					
				case "3":
					System.out.println("Aqui estao seus tweets:");
					try{
						Vector<Tweet> selfTweets = control.tweets(usuario.getUsuario());
						for (int i = 0; i < selfTweets.size(); i++){
							printTweet(selfTweets.get(i));
						}
						System.out.println("Tweets impressos com sucesso! =)");
					}
					catch(MyTwitterException mte){
						System.out.println("Erro! :c \n"+ mte.getMessage());
					}
					
					break;
				
				case "4":
					System.out.println("Aqui estao as informacoes dos seus seguidores:");
					try{
						System.out.println("Voce tem "+ control.numeroSeguidores(usuario.getUsuario()) + " seguidores");
						Vector<Perfil> seguidores = control.seguidores(usuario.getUsuario());
						for(int i=0; i < seguidores.size(); i++){
							System.out.println("Seguidor "+i+": @"+seguidores.get(i).getUsuario());
						}
						System.out.println("Informacoes de seguidores impressas com sucesso! =)");
					}
					catch(MyTwitterException mte){
						System.out.println("Erro! :c \n"+ mte.getMessage());
					}
					
					break;
					
				case "5":
					System.out.println("Digite o usuario de quem voce deseja seguir:");
					try{
						control.seguir(usuario.getUsuario(), scanner.nextLine());
						System.out.println("Usuario seguido com sucesso! =)");
					}
					catch(MyTwitterException mte){
						System.out.println("Erro! :c \n"+ mte.getMessage());
					}
					
					break;
					
				case "6":
					if(usuario.isAtivo() == true){
						System.out.println("Usuario ja ativado!");
					}
					else{
						usuario.setAtivo(true);
						System.out.println("Usuario foi ativado com sucesso!");
					}
					
					break;
					
				case "7":
					if(usuario.isAtivo() == false){
						System.out.println("Usuario ja desativado!");
					}
					try{
						control.cancelarPerfil(usuario.getUsuario());
						System.out.println("Usuario desativado com sucesso!");
					}
					catch(MyTwitterException mte){
						System.out.println("Erro! :c \n"+ mte.getMessage());
					}
					
					break;
					
				case "8":
					System.out.println("Aqui estao as informacoes da sua conta:");
					if (usuario instanceof PessoaFisica){
						System.out.println("Usuario: @"+usuario.getUsuario());
						System.out.println("CPF: "+ ((PessoaFisica)usuario).getCpf());
					}
					else{
						System.out.println("Usuario: @"+usuario.getUsuario());
						System.out.println("CNPJ: "+ ((PessoaJuridica)usuario).getCnpj());
					}
					
					break;
					
				case "9":
					System.out.println("Saindo da conta...\n");
					usuario = null;
					
					break;
					
				case "10":
					System.out.println("Ate a proxima! =D");
					usuario = null;
					loop = false;
				
					break;
					
				default:
					break;
				
				}
				
			}
		}
	}

	private static String mainMenu(String usuario) {
		System.out.println("================================");
		System.out.println("Ola, @"+usuario+"! Bem vindo ao Twitter do Cid :D");
		System.out.println("Melhor twitter da historia =)");
		System.out.println("================================");
		System.out.println(" [1] Postar Tweet");
		System.out.println(" [2] Verificar sua timeline");
		System.out.println(" [3] Verificar seus proprios tweets");
		System.out.println(" [4] Verificar seguidores");
		System.out.println(" [5] Seguir alguem");
		System.out.println(" [6] Ativar Conta");
		System.out.println(" [7] Desativar conta");
		System.out.println(" [8] Consultar informacoes da sua conta");
		System.out.println(" [9] Sair da conta");
		System.out.println(" [10] Sair do programa");
		System.out.println("================================");
		System.out.println("Coloque a opcao desejada : ");
		return scanner.nextLine();
	}
	
	private static String startMenu(){
		System.out.println("================================");
		System.out.println("Twitter do Cid");
		System.out.println("================================");
		System.out.println(" [1] Entrar em uma conta");
		System.out.println(" [2] Criar uma conta");
		System.out.println(" [3] Sair do programa");
		System.out.println("================================");
		System.out.println("Coloque a opcao desejada : ");
		return scanner.nextLine();

	}
	
	private static void printTweet(Tweet tweet){
		System.out.println("Usuario: @" + tweet.getUsuario());
		System.out.println("Tweet: " + tweet.getMensagem());
		System.out.println(" ");
	}
}
