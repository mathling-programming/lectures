Anatomy of Git repositories
===========================

.. graphviz::

   digraph {
      node [ shape = component, fontname = "monospace" ]
      edge [ fontname = "monospace", labelfontname = "monospace" ]
      blob1 [ shape = note, label = "9daeafb", tooltip = "9daeafb9864cf43055ae93beb0afd6c7d144bfa4" ]
      blob2 [ shape = note, label = "3e75765" ]
      blob3 [ shape = note, label = "180cf83" ]
      blob4 [ shape = note, label = "a5bce3f" ]
      subblob [ shape = note, label = "e69de29" ]
      tree1 [ shape = folder, label = "ae5c731" ]
      tree2 [ shape = folder, label = "bffa072" ]
      subtree [ shape = folder, label = "c5a917c" ]

      tree1 -> blob1 [ dir = none, label = "file.dat" ]
      tree1 -> blob2 [ dir = none, label = "newfile.dat" ]
      tree2 -> blob1 [ dir = none, label = "file.dat" ]
      tree2 -> blob3 [ dir = none, label = "oldname.dat" ]
      tree1 -> blob3 [ dir = none, label = "newname.dat" ]
      tree2 -> blob4 [ dir = none, label = "deleted.dat" ]
      subtree -> subblob [ dir = none, label = "subfile.dat" ]
      tree1 -> subtree [ dir = none, label = "dir/" ]
      tree2 -> subtree [ dir = none, label = "dir/" ]

      commit1 [ tooltip = "git mv oldname.dat newname.dat\ngit rm deleted.dat\ngit add newfile.dat", fontsize = 12,
                label = "5ecdca016974fe5faa884c24515f3e6302209d7e\l\lAuthor: John R. Hacker <jrhacker@example.com>\lDate: Fri Mar 10 18:45:22 2023 +0300\l\llatest commit here\l"]
      commit4 [ label = "92d8745\linitial commit" ]
      commit3 [ label = "7b81d07" ]
      commit2 [ label = "eb04ee5" ]
      commit6 [ label = "fa3f8af" ]
      commit5 [ label = "0941846" ]
      commit1 -> tree1
      commit2 -> tree2
      commit1 -> commit2
      commit2 -> commit3
      commit3 -> commit4
      commit5 -> commit6
      commit6 -> commit3
      head [ shape = point, xlabel = "HEAD", fontname = "monospace" ]
      head -> commit1
      branch1 [ shape = invhouse, label = "devel" ]
      branch1 -> commit5
      branch2 [ shape = invhouse, label = "stable" ]
      branch2 -> commit1
      tag1 [ shape = cds, label = "v1.0.0" ]
      tag1 -> commit3
   }

.. graphviz::

   digraph {
     rankdir = LR
     label = "Legend"
     bgcolor = lightgray
     node [ fontname = "times-italic" ]
     edge [ style = "invis" ]
     ex_blob [ shape = note, label = "Blob object" ]
     ex_tree [ shape = folder, label = "Tree object" ]
     ex_commit [ shape = commit, label = "Commit object" ]
     ex_tag [ shape = cds, label = "Tag (object)" ]
     ex_branch [ shape = invhouse, label = "Branch" ]

     ex_blob -> ex_tree -> ex_commit -> ex_tag -> ex_branch

   }

+----------+----------+--------+
| Ref      | Tracking | Global |
+==========+==========+========+
| HEAD     | Yes      | No     |
+----------+----------+--------+
| tags     | No       | Yes/No |
+----------+----------+--------+
| branches | Yes      | No     |
+----------+----------+--------+
