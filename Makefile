BINDIR = /usr/bin
DOTF = $(HOME)/.config
fetchname=bunnydelic

install:
	@echo "Creating executable..."
	@chmod 755 source
	@echo "Getting sudo access to create a binary"
	@sudo cp source $(BINDIR)/$(fetchname)
	@echo "Generating config file in .config/$(fetchname)..."
	@mkdir $(DOTF)/$(fetchname) && cp config.py ascii.py $(DOTF)/$(fetchname)/
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


