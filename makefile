SUBDIRS = LabSheets/images LabSheets

subdirs:
		for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
		done
