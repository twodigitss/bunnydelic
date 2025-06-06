BINDIR = /usr/bin
DOTF = $(HOME)/.config
fetchname=bfch

install:
	@echo "Creating executable..."
	@echo "Giving permissions to execute..."
	@chmod 755 source
	@echo "Getting sudo access to create a binary at /usr/bin/ directory..."
	@sudo cp source $(BINDIR)/$(fetchname)
	@echo "Generating config file in .config/$(fetchname)..."
	# thank you RafaFonPessoa for letting me know!
	@mkdir $(DOTF)/$(fetchname) && cp config.py $(DOTF)/$(fetchname)/
	@echo "Done! Execute as $(fetchname)"

uninstall:
	@echo "deleting config folder and binaries..."
	@sudo rm -rf $(BINDIR)/$(fetchname)
	@sudo rm -rf $(DOTF)/$(fetchname)/
	@echo "Done"

help:
	@echo "Use:"
	@echo "  make install   - Installs this program."
	@echo "  make uninstall - Removes this program."
	@echo "  Or Also you can design a alias shortcut in case you dont want"
	@echo "  to install. like <alias bn='./$HOME/github/bunnydelic/source'>"


