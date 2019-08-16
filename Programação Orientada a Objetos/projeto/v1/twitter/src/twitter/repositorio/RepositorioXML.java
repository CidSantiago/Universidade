package twitter.repositorio;

import twitter.perfils.Perfil;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Vector;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;

import twitter.repositorio.exceptions.*;

public class RepositorioXML implements IRepositorioUsuario {

	public static final String PERFIS_DB_XML_NAME = "PerfisDB.xml";
	
	private Vector<Perfil> perfis = null;
	
	public RepositorioXML() {
		try {
			loadData();
		} catch (FileNotFoundException fnfe) {
			this.perfis = new Vector<Perfil>();
			try {
				saveData();
			} catch (IOException ioe) {
				ioe.printStackTrace();
			}
		}
	}
	
	@Override
	public void cadastrar(Perfil usuario) throws  UJCException, CadastroException {
		
		if( buscar(usuario.getUsuario()) == null){
			perfis.addElement(usuario);
			
			try{
				saveData();
			}
			catch (IOException ioe){
				throw new CadastroException("Erro no cadastro da conta!" + ioe.getMessage(), usuario.getUsuario());
			}
		}
		else{
			throw new UJCException ("Usuario já cadastrado!", usuario.getUsuario());
		}
	
	}
	

	@Override
	public Perfil buscar(String usuario) {
		for(int i = 0; i < perfis.size(); i++){
			Perfil perfil = perfis.elementAt(i);
			if(perfil.getUsuario().equals(usuario)){
				return perfil;
			}
		}
		return null;
	}

	@Override
	public void atualizar(Perfil usuario) throws UNCException, IOException{
		Perfil perfil;
		perfil = buscar(usuario.getUsuario());
		if(perfil != null){
			perfil = usuario;
		}
		else{
			throw new UNCException("Usuário não encontrado!", usuario.getUsuario());
		}
		
		try{
			saveData();
		}
		catch (IOException ioe){
			throw new IOException(ioe);
		}
	}
	
	@SuppressWarnings("unchecked")
	private void loadData() throws FileNotFoundException {

		XStream xstream = new XStream(new DomDriver());
		xstream.alias("Perfil", Perfil.class);
		perfis = ((Vector<Perfil>) xstream.fromXML(new FileReader(PERFIS_DB_XML_NAME), Vector.class));
		System.out.println(perfis.size());
	}

	private void saveData() throws IOException {
		XStream xstream = new XStream();
		xstream.alias("Perfis", Perfil.class);
		xstream.toXML(perfis, new FileWriter(PERFIS_DB_XML_NAME));
	}

}
