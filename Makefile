BINDIR = /usr/bin
DOTF   = $(HOME)/.config
fetchname=bunnydelic

install:
	#creating binary	
	@chmod 755 source
	@sudo cp source $(BINDIR)/$(fetchname)
	#generating config file in .config/$(fetchname)
	@mkdir $(DOTF)/$(fetchname) && cp config.py $(DOTF)/$(fetchname)/

uninstall:
	@sudo rm -rf $(BINDIR)/$(fetchname)
	@sudo rm -rf $(DOTF)/$(fetchname)/
	#Done
