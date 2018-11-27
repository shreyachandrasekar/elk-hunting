// Brian Richer
// ************
// Ethical hacking email spoofer
//
// Usage: 

import java.util.*;
import javax.mail.Authenticator;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import javax.mail.PasswordAuthentication;
import static java.lang.System.*;

import java.io.*;

public class SpoofEmail {

	static final String from      = "no-reply@ashleymadisonlife.com";
	static final String subject   = "You've got a new message request!";
	static final String siteip    = "localhost";

	/* HTTP port that faked site is running on */
	static final String siteport  = "5000";

	static final String body      = "Click <a href='http://" + siteip + ":" + siteport + "'>here</a> to resolve all pending invitations.";
	static final String smtp_host = "localhost";
	static final String smtp_port = "25";
	static final String smtp_user = "test@test.com";
	static final String smtp_pass = "test";

	public static void main(String [] args) throws IOException {
		System.out.println("Running email spoofer with " + (args.length) + " emails...");
		for (int i=0; i<args.length; i++){
			System.out.println("Reading email list " + args[i]);
			parseList(args[i]);
		}
	}

	private static void parseList(String filename) throws IOException {
		//SMTP server
		Properties prop = new Properties();
		prop.put("mail.smtp.host", smtp_host);
		prop.put("mail.smtp.auth", "true");
		prop.put("mail.smtp.starttls.enable", "true");
		prop.put("mail.smtp.port", smtp_port);
		
		Authenticator auth = new Authenticator() {
			protected PasswordAuthentication getPasswordAuthentication() {
				return new PasswordAuthentication(smtp_user, smtp_pass);
			}
		};

		Session session = Session.getInstance(prop, auth);

		try (Scanner emails = new Scanner(new File(filename))) {
			while (emails.hasNextLine()) {

				String email = emails.nextLine();
				System.out.println("Sending email to: " + email);

				try {
					MimeMessage msgobj = new MimeMessage(session);
					msgobj.setFrom(new InternetAddress(from));
					msgobj.setSubject(subject);
					msgobj.setText(body, "utf-8", "html");
					msgobj.setRecipients(Message.RecipientType.TO, InternetAddress.parse(email));
					Transport.send(msgobj);
				}
				catch(MessagingException exp) {
					exp.printStackTrace();
					throw new RuntimeException(exp);
				}
			}
		}
	}
}
