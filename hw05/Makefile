# *****************************************************************
#
# Starter Makefile
#
# Contains rules for:
#
# - .x (arm executable target)
# - .o (arm object file)
# - .PHONY (all, clean and test)
#
#
# Uses the following variables (built-in and user-defined):
#
# CC = C compiler (gcc)
# CFLAGS = compiler options (e.g. -g)
# LINKER_FLAGS = specify libraries to link in
# $@ = target
# $^ = all dependencies
# $< = first dependency only (not used in this solution)
#
# Generic "rule" terminology:
#
# target:dependency
# [TAB] <CMD1>
# [TAB] <CMD2>
#
# GCC options used in this Makefile:
#
# -c = "compile only"
# -o = "output filename"
# -g = "debug mode"
#
# Note1: if you use a filename other than "makefile", use the
# 	 -f option to enable make to use it:
# 	 e.g.  make -f my_make_file.mak
#
# Note2: .PHONY tells make that the rule's target is not 
#        actually a file (to be created or searched for).
#
# Note3: When make runs without any rules specified on the
#        command line, it will make (by default) the FIRST
#        rule found in the makefile. Hence, it is common
#        to have a rule named "all" listed first (as below).
# 
# ***************************************************************


# -----------------------
# ------ includes -------
# -----------------------

-include ./path.mak

# --------------------------------
# ------ user-defined vars -------
# --------------------------------

CC := $(LINUXarm_GCC)
CFLAGS := -g
LINKER_FLAGS := -lstdc++

# -----------------------
# ------ make all -------
# -----------------------

# The "all" rule commonly specifies all executable targets to
# be built. Note, the user has full control over what the "all"
# rule builds. In this solution, we only have one target.
# However, in the final Beagle makefile, you'll see more
# targets listed. 


.PHONY : all
all : app.arm


# -----------------------------------
# ------ executable rule (.x) -------
# -----------------------------------
%.arm : %.o
		$(CC) $(CFLAGS) $< -o $@
		@echo; echo $@ successfully created; echo
# ---------------------------------------------------
# ------ intermeditate object files rule (.o) -------
# ---------------------------------------------------
%.o : %.c
		$(CC) $(CFLAGS) -c $< -o $@

# ----------------------
# ----- clean all ------
# ----------------------

# The "clean" rule should remove all files created by
# the makefile (e.g. the executables and intermediate
# files).

.PHONY : clean
clean :
		rm -rf app.arm
		rm -rf app.o


# -------------------------------------
# ----- basic debug for Makefile ------
#
# -----     example only         ------
# -------------------------------------

# We use test to print out the user-defined variables to
# make sure they are set properly - this helps with 
# debugging makefile errors.



.PHONY : test
test:
		@echo CC = $(CC)
