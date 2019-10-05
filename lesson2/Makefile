COMPILER_FLAGS=-Werror -g -ggdb3 -O2  # AUTOGEN
    
CLANG_COMPILER_WARNINGS=-Wall # AUTOGEN
GCC_COMPILER_WARNINGS=-Wall # AUTOGEN
GXX_COMPILER_WARNINGS=-Wall # AUTOGEN
COMPILER_WARNINGS=$(GCC_COMPILER_WARNINGS) # AUTOGEN
COMPILER_WARNINGS=$(GXX_COMPILER_WARNINGS) # AUTOGEN
COMPILER_WARNINGS=$(CLANG_COMPILER_WARNINGS) # AUTOGEN
CC=clang # AUTOGEN
# CC=gcc # AUTOGEN
# CC=cc # AUTOGEN
# CC=g++ # AUTOGEN
    
EXE= # AUTOGEN
LDLIBS= # AUTOGEN
CFLAGS=$(COMPILER_FLAGS) $(COMPILER_WARNINGS) # AUTOGEN
NAME=lesson2
OBJDIR=.o

TARGET_OBJECTS=$(OBJDIR)/lesson2.o

EXTRA_CFLAGS=-std=c++11

$(OBJDIR)/%.o: %.cpp
	@echo $(CXX) $(EXTRA_CFLAGS) $(CFLAGS) -c -o $@ $<
	@$(CXX) $(EXTRA_CFLAGS) $(CFLAGS) -c -o $@ $<

#
# link
#
TARGET=$(NAME)$(EXE)
$(TARGET): $(TARGET_OBJECTS)
	$(CXX) $(TARGET_OBJECTS) $(LDLIBS) -o $(TARGET)

#
# To force clean and avoid "up to date" warning.
#
.PHONY: clean
.PHONY: clobber

clean:
	rm -rf $(TARGET) $(OBJDIR)/*.o

clobber: clean
	mkdir -p $(OBJDIR)

all: $(TARGET) 
# DO NOT DELETE

.o/lesson2.o: point.h ansi.h terminal.h /usr/include/sys/ioctl.h
.o/lesson2.o: /usr/include/sys/ttycom.h /usr/include/sys/ioccom.h
.o/lesson2.o: /usr/include/sys/_types.h /usr/include/sys/cdefs.h
.o/lesson2.o: /usr/include/sys/_symbol_aliasing.h
.o/lesson2.o: /usr/include/sys/_posix_availability.h
.o/lesson2.o: /usr/include/machine/_types.h /usr/include/i386/_types.h
.o/lesson2.o: /usr/include/sys/_pthread/_pthread_types.h
.o/lesson2.o: /usr/include/sys/filio.h /usr/include/sys/sockio.h
.o/lesson2.o: /usr/include/sys/appleapiopts.h /usr/include/termios.h
.o/lesson2.o: /usr/include/sys/termios.h
.o/lesson2.o: /usr/include/sys/_types/_posix_vdisable.h
.o/lesson2.o: /usr/include/sys/ttydefaults.h /usr/include/_types.h
.o/lesson2.o: /usr/include/sys/_types/_pid_t.h /usr/include/unistd.h
.o/lesson2.o: /usr/include/sys/unistd.h /usr/include/sys/_types/_seek_set.h
.o/lesson2.o: /usr/include/sys/_types/_size_t.h
.o/lesson2.o: /usr/include/_types/_uint64_t.h /usr/include/_types/_uint32_t.h
.o/lesson2.o: /usr/include/Availability.h /usr/include/AvailabilityInternal.h
.o/lesson2.o: /usr/include/sys/_types/_ssize_t.h /usr/include/machine/types.h
.o/lesson2.o: /usr/include/i386/types.h /usr/include/sys/_types/_int8_t.h
.o/lesson2.o: /usr/include/sys/_types/_int16_t.h
.o/lesson2.o: /usr/include/sys/_types/_int32_t.h
.o/lesson2.o: /usr/include/sys/_types/_int64_t.h
.o/lesson2.o: /usr/include/sys/_types/_u_int8_t.h
.o/lesson2.o: /usr/include/sys/_types/_u_int16_t.h
.o/lesson2.o: /usr/include/sys/_types/_u_int32_t.h
.o/lesson2.o: /usr/include/sys/_types/_u_int64_t.h
.o/lesson2.o: /usr/include/sys/_types/_intptr_t.h
.o/lesson2.o: /usr/include/sys/_types/_uintptr_t.h
.o/lesson2.o: /usr/include/sys/_types/_uid_t.h
.o/lesson2.o: /usr/include/sys/_types/_gid_t.h
.o/lesson2.o: /usr/include/sys/_types/_off_t.h
.o/lesson2.o: /usr/include/sys/_types/_useconds_t.h
.o/lesson2.o: /usr/include/sys/_types/_null.h /usr/include/sys/select.h
.o/lesson2.o: /usr/include/sys/_types/_fd_def.h
.o/lesson2.o: /usr/include/sys/_types/_timespec.h
.o/lesson2.o: /usr/include/sys/_types/_timeval.h
.o/lesson2.o: /usr/include/sys/_types/_time_t.h
.o/lesson2.o: /usr/include/sys/_types/_suseconds_t.h
.o/lesson2.o: /usr/include/sys/_types/_sigset_t.h
.o/lesson2.o: /usr/include/sys/_types/_fd_setsize.h
.o/lesson2.o: /usr/include/sys/_types/_fd_set.h
.o/lesson2.o: /usr/include/sys/_types/_fd_clr.h
.o/lesson2.o: /usr/include/sys/_types/_fd_isset.h
.o/lesson2.o: /usr/include/sys/_types/_fd_zero.h
.o/lesson2.o: /usr/include/sys/_types/_fd_copy.h /usr/include/sys/_select.h
.o/lesson2.o: /usr/include/sys/_types/_dev_t.h
.o/lesson2.o: /usr/include/sys/_types/_mode_t.h
.o/lesson2.o: /usr/include/sys/_types/_uuid_t.h /usr/include/gethostuuid.h
