BINDIR = /usr/bin
DOTF = $(HOME)/.config
fetchname=bunnydelic

install:
	#creating executable...
	@chmod 755 source
	#getting sudo access to create a binary
	@sudo cp source $(BINDIR)/$(fetchname)
	#generating config file in .config/$(fetchname)...
	@mkdir $(DOTF)/$(fetchname) && cp config.py ascii.py $(DOTF)/$(fetchname)/
	#done

uninstall:
	#deleting config folder and binaries...
	@sudo rm -rf $(BINDIR)/$(fetchname)
	@sudo rm -rf $(DOTF)/$(fetchname)/
	#Done
