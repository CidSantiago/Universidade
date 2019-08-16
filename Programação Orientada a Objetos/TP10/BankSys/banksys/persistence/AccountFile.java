package banksys.persistence;

import java.util.Vector;

import banksys.account.AbstractAccount;
import banksys.persistence.exception.AccountCreationException;
import banksys.persistence.exception.AccountDeletionException;
import banksys.persistence.exception.AccountNotFoundException;

public class AccountFile implements IAccountRepository {
	
	File diretorio = new File ("/DB");
	private AbstractAccount account = null;

	public AccountFile() {
		diretorio.mkdir();
		this.accounts = new AbstractAccount;
	}

	public void create(AbstractAccount account) throws AccountCreationException{
		if (this.findAccount(account.getNumber()) != null) {
			File conta = new File(diretorio,account.getNumber()+".txt"));
			
		} else {
			throw new AccountCreationException("Account alredy exist!", account.getNumber());
		}

	public void delete(String number) throws AccountDeletionException {
		
		if (account != null) {
			;
		} else {
			throw new AccountDeletionException("Account doesn't exist!", number);
		}
	}

	}
}