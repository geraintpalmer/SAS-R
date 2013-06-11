SUBDIRS = Lab_Sheets Lab_Sheets/images

subdirs:
		for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
		done
