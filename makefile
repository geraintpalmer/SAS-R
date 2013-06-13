SUBDIRS = Lab_Sheets/images Lab_Sheets 

subdirs:
		for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
		done
