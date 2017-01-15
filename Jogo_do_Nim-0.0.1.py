def computador_escolhe_jogada(n,m):
	p = 1

	if(n <= m):
		if(n<m):
			n = n - n
			if ( n == 1):
				print("O computador tirou uma peça.")
			else:
				print("O computador tirou",n,"peças.")
		else:
			n = n - m
			if ( m == 1):
				print("O computador tirou uma peça.")
			else:
				print("O computador tirou",m,"peças.")
			
	else:
		while(p <= m):
			if ( (m + 1) % (n - p) == 0):
				n = n - p
				if ( p == 1):
					print("O computador tirou uma peça.")
				else:
					print("O computador tirou",p,"peças.")
				p = m + 1
			else:
				p = p + 1
 
		
	return n




def usuario_escolhe_jogada(n,m):
	p = int(input("Quantas peças você vai tirar? "))
	while ( p > m or p > n ):
		p = int(input("Oops! Jogada inválida! Tente de novo. "))
	n = n - p
	if(p == 1):
		print("Voce tirou uma peça.")
	else:
		print("Voce tirou",p,"peças.")
	return n


def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	
	if ( ( (m + 1) % n) == 0):
		print("Voce começa!")
		while( n > 0):
			if ( n != 0 ):
				n = usuario_escolhe_jogada(n,m)
				if ( n == 0 ):
					print("Fim do jogo! Voce ganhou!")
				else:
					print("Agora restam",n,"peças no tabuleiro")
			if (n !=0):
				n = computador_escolhe_jogada(n,m)
				if (n == 0):
					print("Fim do jogo! Computador Ganhou!")
					
				else:
					print("Agora restam",n,"peças no tabuleiro.")
	
	else:
		print("Computador começa!")
		while( n > 0):
			if ( n != 0 ):
				n = computador_escolhe_jogada(n,m)
				if ( n == 0 ):
					print("Fim do jogo! Computador Ganhou!")
				else:
					print("Agora restam",n,"peças no tabuleiro.")
			if (n !=0):
				n = usuario_escolhe_jogada(n,m)
				if (n == 0):
					print("Fim do jogo! Voce Ganhou!")
					
				else:
					print("Agora restam",n,"peças no tabuleiro.")	
	return 0

def campeonato():
	i = 1
	vc = 0
	pc = 0
	while(i <= 3):
		print("***** Rodada ",i,"****")
		n = int(input("Quantas peças ? "))
		m = int(input("Limite de peças por jogada? "))
	
		if ( ( (m + 1) % n) == 0):
			print("Voce começa!")
			while( n > 0):
				if ( n != 0 ):
					n = usuario_escolhe_jogada(n,m)
					if ( n == 0 ):
						vc = vc + 1
						print("Fim do jogo !Voce ganhou!")
					else:
						print("Agora restam",n,"peças no tabuleiro.")
				if (n !=0):
					n = computador_escolhe_jogada(n,m)
					if (n == 0):
						pc = pc + 1
						print("Fim do jogo! Computador Ganhou!")
					
					else:
						print("Agora restam",n,"peças no tabuleiro.")
			i = i + 1
	
		else:
			print("Computador começa!")
			while( n > 0):
				if ( n != 0 ):
					n = computador_escolhe_jogada(n,m)
					if ( n == 0 ):
						pc = pc + 1
						print("Fim do jogo! Computador Ganhou!")
					else:
						print("Agora restam",n,"peças no tabuleiro.")
				if (n !=0):
					n = usuario_escolhe_jogada(n,m)
					if (n == 0):
						vc = vc + 1
						print("Fim do jogo! Voce Ganhou!")
					
					else:
						print("Agora restam",n,"peças no tabuleiro.")
			i = i + 1


		print("Placar: Você",vc," X Computador",pc)
		
	print("**** Final do Jogo ****")
	print(" Placar: Você",vc," X Computador",pc)
	return 0





print("Bem-vindo ao Jogo NIM! Escolha:")
print("1 - para jogar uma partida isolada ")
n = int(input("2 - para jogar um campeonato "))


if ( n == 1):
	print("Voce escolheu uma partida!")
	partida()
else:
   print("Voce escolheu um campeonato!")
   campeonato()


 


