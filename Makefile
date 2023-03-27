#


PID  = 2023-S1-MX-55

help:
	@echo PID=$(PID)
	@echo WORK_LMT=$(WORK_LMT)
	@echo Targets here:
	@echo "   runs      - make the run1/run2/... files"
	@echo "   summary   - update the project summary index"
	@echo "               https://taps.lmtgtm.org/lmtslr/$(PID)"


runs:
	./mk_runs.py


summary:
	@for p in $(PID); do \
	(echo $$p;  cd $(WORK_LMT)/$$p; mk_summary1.sh > README.html); \
	done