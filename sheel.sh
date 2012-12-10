#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

svn co http://svn.enlightenment.org/svn/e/trunk/PROTO/emote emote; \
cd emote; \
SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
VERSION=$(cat configure.ac | grep "emote" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
PKG_VERSION=$VERSION.$SVNREV; \
cd ..; \
tar -Jcf emote-$PKG_VERSION.tar.xz emote/ --exclude .svn --exclude .*ignore

